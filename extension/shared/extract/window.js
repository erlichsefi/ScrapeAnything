function get_viewpoint(){
    const viewpointscroll = window.pageYOffset || document.documentElement.scrollTop;
    const viewportHeight = window.innerheight || document.documentElement.clientHeight;
    return viewpointscroll,viewportHeight
}
const {viewpointscroll,viewportHeight} = get_viewpoint()
console.log(viewpointscroll)
console.log(viewportHeight)