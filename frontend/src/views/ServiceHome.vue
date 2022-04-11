<template>

    <BlogHeader/>

    <ServiceList/>

    <BlogFooter/>

</template>

<script>
    import BlogHeader from '@/components/BlogHeader.vue'
    import BlogFooter from '@/components/BlogFooter.vue'
    import ServiceList from '@/components/ServiceList.vue'


    export default {
        name: 'Home',
        components: {BlogHeader, BlogFooter, ServiceList}
    }
</script>