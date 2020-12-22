<template>
  <div class="container">

    <h1>BrAPI test server v2 call</h1>

    <div class="mt-5">
      <h3>Raw data</h3>
      <div class="">
        {{info}}
      </div>
    </div>

    <div class="mt-5">
      <h3>Crop names</h3>

      <div>
        <ul>
          <li v-for="c in c_data" v-bind:key="c">{{c}}</li>
        </ul>

      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'brapicalls',
  data() {
    return{
      info: null,
      c_data: null
    }
  },
  mounted(){
    axios
      .get('https://test-server.brapi.org/brapi/v2/commoncropnames')
      .then(response => (this.info = response,
          this.c_data = response.data.result.data))
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
