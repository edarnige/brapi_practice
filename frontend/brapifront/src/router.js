import Vue from "vue";
import Router from "vue-router";

// import App from "./App.vue"
import Tasks from "./views/Tasks.vue";
import Test from "./views/Test";

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
            path: "/test",
            name: "test",
            components: {default: Test}
        },

    ]
})