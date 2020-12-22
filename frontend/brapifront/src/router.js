import Vue from "vue";
import Router from "vue-router";

// import App from "./App.vue"
import Tasks from "./views/Tasks.vue";
import BrAPICalls from "./views/BrAPICalls.vue";
import Programs from "./views/Programs";

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
        {
            path: "/brapi/programs",
            name: "programs",
            components: {default: Programs}
        },

    ]
})