
export default function refresh(){
    location.reload();
}

export default function back(){
    window.history.back();
}

export default function go_to_url(url){
    window.location.href = url;
}