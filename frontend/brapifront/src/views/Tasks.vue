<template>
  <div>
    <h1>Taskforce</h1>

    <hr>

    <div class="columns">
      <div class="column is-3 is-offset-3">

        <form>
          <h2>Add task</h2>

          <div class="field">
            <label for="" class="label">Description</label>
            <div class="control">
              <input type="text" v-model="description">
            </div>
          </div>

          <div class="field">
            <label for="" class="label">Status</label>
            <div class="control">
              <div class="select">
                <select v-model="status">
                  <option value="todo">To do</option>
                  <option value="done">Done</option>
                </select>
              </div>
            </div>
          </div>

          <div class="field">
            <div class="control">
              <b-button @click="addTask" variant="primary">Submit</b-button>
            </div>
          </div>

        </form>

      </div>
    </div>

    <div class="columns">
      <div class="column is-6">
        <h2>To Do</h2>
        <div class="todo">
          <div class="card" v-for="task in tasks" v-bind:key="task.id">
            <div class="card-content">{{ task.description }}</div>
            <footer class="card-footer">
              <a href="" class="card-footer-item">Done</a>
            </footer>
          </div>
        </div>
      </div>

      <div class="column is-6">
        <h2>Done</h2>
        <div class="done">
          <div class="card" v-for="task in tasks" v-bind:key="task.id">
            <div class="card-content">{{ task.description }}</div>
          </div>
        </div>
      </div>

    </div>

  </div>
</template>

<script>

import axios from 'axios';

export default {
  name: 'tasks',
  data() {
    return{
      tasks: [],
      description: '',
      status: 'todo'
    }
  },
  mounted(){
    this.getTasks()
  },
  methods: {
    getTasks(){
      axios({
        method: 'get',
        url: 'http://localhost:8000/tasks/'
      }).then(response => this.tasks = response.data)
    },
    addTask() {
      if(this.description){
        axios({
          method: 'post',
          url: 'http://localhost:8000/tasks/',
          data: {
            description: this.description,
            status: this.status
          }
        }).then(response =>{
          let newTask = {
            'id': response.data.id,
            'description' : this.description,
            'status': this.status
          }

          this.tasks.push(newTask)
          //reset
          this.description = ''
              this.status = 'todo'
        }).catch(error => {
          console.log(error)
        })
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
