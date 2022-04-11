<template>

    <BlogHeader/>

    <div v-if="service !== null" class="grid-container">
        <div>
            <h1 id="title">{{ service.title }}</h1>
            <p id="subtitle">
                本文由 {{ service.author.username }} 发布于 {{ formatted_time(service.created) }}
            </p>
          <div v-html="service.body_html" class="article-body"></div>
        </div>

    </div>


    <BlogFooter/>

</template>

<script>
    import BlogHeader from '@/components/BlogHeader.vue'
    import BlogFooter from '@/components/BlogFooter.vue'

    import axios from 'axios';


    export default {
        name: 'ServiceDetail',
        components: {BlogHeader, BlogFooter},
        data: function () {
            return {
                service: null
            }
        },
        mounted() {
            axios
                .get('/api/service/' + this.$route.params.id)
                .then(response => (this.service = response.data))
        },
        methods: {
            formatted_time: function (iso_date_string) {
                const date = new Date(iso_date_string);
                return date.toLocaleDateString()
            }
        },
        computed: {
            isSuperuser() {
                return localStorage.getItem('isSuperuser.myblog') === 'true'
            }
        }
    }
</script>

<style scoped>
    .grid-container {
        display: grid;
        grid-template-columns: 3fr 1fr;
    }


    #title {
        text-align: center;
        font-size: x-large;
    }

    #subtitle {
        text-align: center;
        color: gray;
        font-size: small;
    }

</style>

<style>
    .article-body p img {
        max-width: 100%;
        border-radius: 50px;
        box-shadow: gray 0 0 20px;
    }

    .toc ul {
        list-style-type: none;
    }

    .toc a {
        color: gray;
    }
</style>