import pickle

from flask import Flask, jsonify, safe_join, send_from_directory
from flask_cors import cross_origin, CORS

STATIC_DIR = '../client/dist'
ASSETS_DIR = './assets'

app = Flask(__name__,
            static_folder=STATIC_DIR,
            )

cors = CORS(app, resources={r"*": {"origins": "*"}})

color_df = pickle.load(open('../data/color/color.pkl', 'rb'))
actual_df = pickle.load(open('../data/actual/actual.pkl', 'rb'))

pathways = {
    'hallmark': pickle.load(open('../data/pathways/hallmark.pkl', 'rb')),
    'kegg': pickle.load(open('../data/pathways/kegg.pkl', 'rb')),
    'reactome': pickle.load(open('../data/pathways/reactome.pkl', 'rb')),
}



@app.route("/api/pathways/<db>/<pw>")
def pathway(db='', pw=''):
    return jsonify({
        'pw_genes': pathways[db][pw]
    })

@app.route('/')
def catch_all():
    return app.send_static_file("index.html")

@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory(safe_join(STATIC_DIR, ASSETS_DIR), path)

def df_to_apex_data(color_scale_df, actual):
    series = [
        {
            'name': data_type,
            'data': [
                {
                 'x': val[0], # sample ID
                 'y': val[1], # color scale val
                 'value': actual[val[0]][data_type]
                }
                for val in vals.items()
            ]
        }
        for data_type, vals in color_scale_df.iterrows()
    ]
    clinical_series_len = actual[actual['Data type'] == ''].shape[0]
    blank_row = { 'name': '', 'data': [] }
    series.insert(clinical_series_len, blank_row)
    return series[::-1]

def filtered_df(df, genes):
    return df[(df['Gene symbol'].isin(genes)) | (df['Gene symbol'] == '')]


@cross_origin()
@app.route("/api/color/<genes_input>/")
def color(genes_input):
    genes = genes_input.split(' ')

    filtered_scale = filtered_df(color_df, genes)

    series = df_to_apex_data(
        filtered_scale.drop(columns=['Data type', 'Gene symbol']),
        actual_df
    )

    return jsonify({
        'series': series
    })
#
#
# @app.route("/api/phospho/color/<genes_input>/")
# def phospho_color(genes_input):
#     genes = genes_input.split(' ')
#
#     filtered_scale = filtered_df(color_scale_phospho, genes)
#
#     series = df_to_apex_data_phospho(
#         filtered_scale.drop(columns=['Data type', 'Gene symbol']),
#         actual_vals_phospho
#     )
#
#     return jsonify({
#         'series': series
#     })
#
#
# @app.route("/api/phospho/table/<genes_input>/")
# def table_phospho(genes_input):
#     genes = genes_input.split(' ')
#
#     filtered_scale = filtered_df(actual_vals_phospho, genes)
#     df_list = filtered_scale.to_dict(orient='records')
#
#     for i, row in enumerate(df_list):
#         row['idx'] = filtered_scale.index[i]
#
#     return jsonify({
#         'excelData': df_list
#     })
#
#
# @app.route("/api/table/<genes_input>/")
# def table(genes_input):
#     genes = genes_input.split(' ')
#
#     filtered_scale = filtered_df(actual_vals, genes)
#     df_list = filtered_scale.to_dict(orient='records')
#
#     for i, row in enumerate(df_list):
#         row['idx'] = filtered_scale.index[i]
#
#     return jsonify({
#         'excelData': df_list
#     })
#
#
# @app.route("/api/pathways/<db>/<pw>")
# def pathway(db='', pw=''):
#     return jsonify({
#         'pw_genes': pathways[db][pw]
#     })
#
#
# @app.route('/')
# def catch_all():
#     return app.send_static_file("index.html")


# @app.route('/assets/<path:path>')
# def send_assets(path):
#     return send_from_directory(safe_join(STATIC_DIR, ASSETS_DIR), path)
