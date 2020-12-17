import Vue from "vue";
import Router from "vue-router";

// import App from "./App.vue"
import Tasks from "./views/Tasks.vue";
import BrAPICalls from "./views/BrAPICalls.vue";

Vue.use(Router);

export default new Router({
    routes: [
        // {
        //     path: "/",
        //     name: "App",
        //     components: {default: App}
        // },
        {
            path: "/tasks",
            name: "tasks",
            components: {default: Tasks}
        },
        {
            path: "/brapi/calls",
            name: "brapicalls",
            components: {default: BrAPICalls}
        },

    ]
})