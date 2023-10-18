function refresh(){
    location.reload();
}

function back(){
    window.history.back();
}

 function move_to_url(url){
    window.location.href = url;
}

module.exports = {move_to_url,back,refresh};