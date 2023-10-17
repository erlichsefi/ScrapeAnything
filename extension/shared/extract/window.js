export default function get_viewpoint(){
    const viewpointscroll = window.pageYOffset || document.documentElement.scrollTop;
    const viewportHeight = window.innerheight || document.documentElement.clientHeight;

    console.log("viewportHeight="+viewportHeight+"viewportHeight="+viewportHeight)
    return {"viewpointscroll":viewpointscroll,"viewportHeight":viewportHeight}
}
// const {viewpointscroll,viewportHeight} = get_viewpoint()
// console.log(viewpointscroll)
// console.log(viewportHeight)