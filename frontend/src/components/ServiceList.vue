<template>


    <div v-for="service in info.results" v-bind:key="service.url" id="services">

            <div>
                <div class="a-title-container">
                    <router-link
                            :to="{ name: 'ServiceDetail', params: { id: service.id }}"
                            class="service-title"
                    >
                        {{ service.title }}
                    </router-link>
                </div>
                <div>{{ formatted_time(service.created) }}</div>
            </div>

    </div>


    <div id="paginator">
        <span v-if="is_page_exists('previous')">
            <router-link :to="get_path('previous')">
                Prev
            </router-link>
        </span>
        <span class="current-page">
            {{ get_page_param('current') }}
        </span>
        <span v-if="is_page_exists('next')">
            <router-link :to="get_path('next')">
                Next
            </router-link>
        </span>
    </div>

</template>

<script>
    // import axios from 'axios';

    import {ref} from 'vue'
    import {useRoute} from 'vue-router'
    import getServiceData from '@/composables/getServiceData.js'
    import pagination from '@/composables/pagination.js'
    import serviceGrid from '@/composables/serviceGrid.js'
    import formattedTime from '@/composables/formattedTime.js'

    export default {
        name: 'ServiceList',

        //
        //
        // 组合式 A 章节内容
        // 教程末尾两个章节重构的代码
        // 没看到此章的读者请看下面被注释部分的代码
        //
        //

        setup() {
            const info = ref('');
            const route = useRoute();

            const kwargs = ref({page: 0, searchText: ''});
            getServiceData(info, route, kwargs);

            const {
                is_page_exists,
                get_page_param,
                get_path
            } = pagination(info, route);

            const {
                gridStyle
            } = serviceGrid();

            const formatted_time = formattedTime;

            return {
                info,
                is_page_exists,
                get_page_param,
                get_path,
                gridStyle,
                formatted_time,
            }
        },


    }

</script>

<style scoped>
    .image {
        width: 180px;
        border-radius: 10px;
        box-shadow: darkslategrey 0 0 12px;
    }

    .image-container {
        width: 200px;
    }

    .grid {
        padding-bottom: 10px;
    }

    #articles {
        padding: 10px;
    }

    .article-title {
        font-size: large;
        font-weight: bolder;
        color: black;
        text-decoration: none;
    }

    .a-title-container {
        padding: 5px 0 5px 0;
    }

    .category {
        padding: 5px 10px 5px 10px;
        margin: 5px 5px 5px 0;
        font-family: Georgia, Arial, sans-serif;
        font-size: small;
        background-color: darkred;
        color: whitesmoke;
        border-radius: 15px;

    }

    .tag {
        padding: 2px 5px 2px 5px;
        margin: 5px 5px 5px 0;
        font-family: Georgia, Arial, sans-serif;
        font-size: small;
        background-color: #4e4e4e;
        color: whitesmoke;
        border-radius: 5px;
    }

    #paginator {
        text-align: center;
        padding-top: 50px;
    }

    a {
        color: black;
    }

    .current-page {
        font-size: x-large;
        font-weight: bold;
        padding-left: 10px;
        padding-right: 10px;
    }

</style>
