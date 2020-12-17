<template>
  <div>

    <h1>BrAPI calls</h1>

    <div class="">
      {{info}}
    </div>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'brapicalls',
  data() {
    return{
      info: null
    }
  },
  mounted(){
    axios
      .get('https://test-server.brapi.org/brapi/v2/commoncropnames')
      .then(response => (this.info = response))

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
