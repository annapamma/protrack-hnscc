import Vue from 'vue';
import VueApexCharts from 'vue-apexcharts';

import App from './App.vue';
import store from './store';


Vue.config.productionTip = false;


Vue.use(VueApexCharts);
Vue.component('apexchart', VueApexCharts);

new Vue({
  store,
  render: h => h(App),
}).$mount('#app');
