function get_url(){
    const response = window.location.href.substring(0, 60)
    console.log(response);
    return response
}
console.log(get_url())