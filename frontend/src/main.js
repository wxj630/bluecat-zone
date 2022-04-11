import {createApp} from 'vue';
import App from './App.vue';
import router from './router';
import naive from 'naive-ui'


URLSearchParams.prototype.appendIfExists = function (key, value) {
    if (value !== null && value !== undefined) {
        this.append(key, value)
    }
};

const app = createApp(App);
app.use(router);
app.use(naive);


app.mount('#app')
// createApp(App).use(router).mount('#app');



