<template>
    <div id="header">
        <div class="grid">
            <div></div>
            <!-- <el-col :xs="24" :sm="24" :md="4" :lg="4" :xl="4"> -->
                <div style="text-align:center;line-height:50px;">
                    <span style="color:blue;font-size:30px;font-weight:bold;">B</span>
                    <span style="font-size:30px;font-weight:bold;">l</span>
                    <span style="font-size:30px;font-weight:bold;">u</span>
                    <span style="font-size:30px;font-weight:bold;">e</span>
                    <span style="font-size:30px;font-weight:bold;">c</span>
                    <span style="font-size:30px;font-weight:bold;">a</span>
                    <span style="font-size:30px;font-weight:bold;">t</span>
                    <span style="color:green;font-size:30px;">F</span>
                    <span style="font-size:25px;">r</span>
                    <span style="font-size:25px;">o</span>
                    <span style="font-size:25px;">n</span>
                    <span style="font-size:25px;">t</span>
                </div>
            <!-- </el-col> -->
            <!--引入搜索框组件-->
            <SearchButton/>
        </div>

        <hr>
        <div>
            <el-row>
                <el-col :span="12">
                    <el-menu 
                    :default-active="activeIndex"
                        class="el-menu-demo"
                        mode="horizontal"
                        @select="handleSelect"
                    >
                        <el-menu-item index="1"><router-link to="/">首页</router-link></el-menu-item>
                        <el-menu-item index="2"><router-link to="/serviceTemp">Services</router-link></el-menu-item>
                    </el-menu>
                </el-col>
                <el-col :span="12">
                    <div class="login">
                            <div v-if="hasLogin">
                                <div class="dropdown">
                                    <button class="dropbtn">欢迎, {{username}}!</button>
                                    <div class="dropdown-content">
                                        <router-link :to="{ name: 'UserCenter', params: { username: username }}">用户中心</router-link>
                                        <router-link :to="{ name: 'ArticleCreate' }" v-if="isSuperuser">发表文章</router-link>
                                        <router-link to="/" v-on:click.prevent="logout()">登出</router-link>
                                    </div>
                                </div>
                            </div>
                            <div v-else>
                                <router-link to="/login" class="login-link">登录</router-link>
                            </div>
                        </div>
                </el-col>
            </el-row>
        </div>
    </div>
</template>

<script>
    import SearchButton from '@/components/SearchButton.vue';
    import authorization from '@/utils/authorization';

    export default {
        name: 'BlogHeader',
        components: {SearchButton},
        data: function () {
            return {
                username: '',
                hasLogin: false,
                isSuperuser: JSON.parse(localStorage.getItem('isSuperuser.myblog')),
            }
        },
        mounted() {
            authorization().then((data) => [this.hasLogin, this.username] = data);
        },
        methods: {
            logout() {
                localStorage.clear();
                window.location.reload(false);
            },
            refresh() {
                this.username = localStorage.getItem('username.myblog');
            }
        }
    }
</script>

<style scoped>
    /*样式来源: https://www.runoob.com/css/css-dropdowns.html*/
    /* 下拉按钮样式 */
    .dropbtn {
        background-color: mediumslateblue;
        color: white;
        padding: 8px 8px 30px 8px;
        font-size: 16px;
        border: none;
        cursor: pointer;
        height: 16px;
        border-radius: 5px;
    }

    /* 容器 <div> - 需要定位下拉内容 */
    .dropdown {
        position: relative;
        display: inline-block;
    }

    /* 下拉内容 (默认隐藏) */
    .dropdown-content {
        display: none;
        position: absolute;
        background-color: #f9f9f9;
        min-width: 120px;
        box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
        text-align: center;
    }

    /* 下拉菜单的链接 */
    .dropdown-content a {
        color: black;
        padding: 12px 16px;
        text-decoration: none;
        display: block;
    }

    /* 鼠标移上去后修改下拉菜单链接颜色 */
    .dropdown-content a:hover {
        background-color: #f1f1f1
    }

    /* 在鼠标移上去后显示下拉菜单 */
    .dropdown:hover .dropdown-content {
        display: block;
    }

    /* 当下拉内容显示后修改下拉按钮的背景颜色 */
    .dropdown:hover .dropbtn {
        background-color: darkslateblue;
    }
</style>

<style scoped>
    .login-link {
        color: black;
    }

    .login {
        text-align: right;
        padding-right: 5px;
    }

    #header {
        text-align: center;
        margin-top: 20px;
    }

    .grid {
        display: grid;
        grid-template-columns: 1fr 4fr 1fr;
    }
</style>