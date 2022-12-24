<template>
    <div id="container" ref="wrapper">
        <template v-if="show">
            <slot></slot>
        </template>
    </div>
</template>

<script>
export default {
    name: 'VueLayout',
    props: {
        options: Object   //object，包含大屏的宽度和高度，以保持宽高比    
    },
    data() {
        return {
            width:0, //传入的宽
            height:0, //传入的宽
            originalWidth:0, //视口宽度
            originalHeight:0,//视口高度
            dom:null,   //最外层DOM元素
            show: false
        }
    },
    mounted() {
        this.init();
        this.updateSize();
        this.updateScale();
        const self = this;
        window.addEventListener("resize", () =>{   //绑定的全局事件要在组件销毁时解除绑定
            self.init();
            // self.updateScale()
        });
        this.show = true
    },
    beforeUnmount() {
        const self = this;
        window.removeEventListener("resize", () => {
            self.init();
        });
    },
    methods:{
        init() {   
            //获取大屏真实宽高
            this.dom  = this.$refs["wrapper"];
            if(this.options && this.options.width && this.options.height){
                this.width = this.options.width;
                this.height = this.options.height;
            }else{
                this.width = this.dom.clientWidth;
                this.height = this.dom.clientHeight;
            }

            //获取屏幕的宽高
            this.originalWidth = window.screen.width;
            this.originalHeight = window.screen.height;
            
            // console.log(this.width, this.height, this.originalWidth, this.originalHeight);
            this.updateScale()
        },
        updateSize() {  //给外层容器设置宽高
            if(this.width && this.height) {
                this.dom.style.width = `${this.width}px`;
                this.dom.style.height = `${this.height}px`;
            }else{
                this.dom.style.width = `${this.originalWidth}px`
                this.dom.style.height = `${this.originalHeight}px`
            }
        },
        updateScale(){   //控制外层容器缩放
            // const currentWidth = document.body.clientWidth;
            // const currentHeight = document.body.clientHeight;

            // const realWidth = this.width || this.originalWidth;
            // const realHeight = this.height || this.originalHeight;

            const widthScale = 1;
            const heightScale = 1;
            this.dom.style.transform = `scale(${widthScale}, ${heightScale})`
        }
    }
}
</script>

<style lang="stylus">
    #container
        position fixed
        top 0
        left 0
        overflow hidden
        z-index 10
        transform-origin left top
</style>
