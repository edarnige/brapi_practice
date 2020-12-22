<template>
  <div class="container">

    <h1>Programs</h1>

    <div class="mt-5">
      <h3>Raw data</h3>
      <div class="">
        {{info}}
      </div>
    </div>

    <div class="mt-5">
      <h3>Program table</h3>
      <div>
        <b-table striped :items="p_data"></b-table>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'programs',
  data() {
    return{
      info: null,
      p_data: null
    }
  },
  mounted(){
    axios
      .get('http://localhost:8000/programs')
      .then(response => (this.info = response,
          this.p_data = response.data.result.data))

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
