
export default function refresh(){
    location.reload();
}

export default function back(){
    window.history.back();
}

export default function move_to_url(url){
    window.location.href = url;
}