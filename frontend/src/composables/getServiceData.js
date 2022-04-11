import axios from 'axios';
import {onMounted, watch} from 'vue'

export default function getServiceData(info, route, kwargs) {
    const getData = async () => {

        const queryPage = route.query.page !== undefined ? parseInt(route.query.page) : 1;
        if (kwargs.value.page === queryPage && kwargs.value.searchText === route.query.search) {
            return
        }

        let url = '/api/service';

        let params = new URLSearchParams();
        params.appendIfExists('page', route.query.page);

        const paramsString = params.toString();
        if (paramsString.charAt(0) !== '') {
            url += '/?' + paramsString
        }

        const response = await axios.get(url);


        info.value = response.data;
        kwargs.value.page = queryPage;
    };

    onMounted(getData);

    watch(route, getData);
}