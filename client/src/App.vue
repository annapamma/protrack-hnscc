<template>
  <div id="app">
      <logo-container />
      <cptac-description />
      <div class="main">
        <input-container />
        <heatmap-container />
      </div>
  </div>
</template>

<script>
import CptacDescription from '@/components/CptacDescription';
import HeatmapContainer from '@/components/HeatmapContainer.vue';
import InputContainer from '@/components/InputContainer.vue';
import LogoContainer from '@/components/LogoContainer.vue';

export default {
  components: {
    CptacDescription,
    HeatmapContainer,
    InputContainer,
    LogoContainer,
  },
};
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
    width: 99vw;
    height: 100vh;
    margin: 0 auto;
  }

  .main {
    display: flex;
    flex-direction: row;
    height: 85%;
      /*background: pink;*/
  }
</style>
