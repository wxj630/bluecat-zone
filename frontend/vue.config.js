module.exports = {
    devServer: {
        proxy: {
            // detail: https://cli.vuejs.org/config/#devserver-proxy
            '/api': {
                target: `http://127.0.0.1:8000/api`,
                changeOrigin: true,
                pathRewrite: {
                    '^/api': ''
                }
            },
            '/recommand_qa': {
                target: `https://192.168.190.63:5001/military_camp_recommand_service`,
                changeOrigin: true,
                pathRewrite: {
                    '^/recommand_qa': ''
                }
            }
        }
    }
};