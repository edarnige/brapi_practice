import Vue from 'vue';
import App from './App.vue';

import router from "./router";

// bootstrap
import{BootstrapVue, IconsPlugin} from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

Vue.config.productionTip = false;
// bootstrap
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);

export default new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
