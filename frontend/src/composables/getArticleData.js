import axios from 'axios';
import {onMounted, watch} from 'vue'


export default function getArticleData(info, route, kwargs) {
    const getData = async () => {

        const queryPage = route.query.page !== undefined ? parseInt(route.query.page) : 1;
        if (kwargs.value.page === queryPage && kwargs.value.searchText === route.query.search) {
            return
        }

        let url = '/api/article';

        let params = new URLSearchParams();
        // params.append('page', route.query.page);
        // params.append('search', route.query.search);
        params = appendIfExists(params, 'page', route.query.page)
        params = appendIfExists(params, 'search', route.query.search)

        const paramsString = params.toString();
        if (paramsString.charAt(0) !== '') {
            url += '/?' + paramsString
        }

        const response = await axios.get(url);


        info.value = response.data;
        kwargs.value.page = queryPage;
        kwargs.value.searchText = route.query.search;
    };

    onMounted(getData);

    watch(route, getData);
}

function appendIfExists(params, key, value) {
    if (value !== null && value !== undefined) {
        params.append(key, value)
    }
    return params
}