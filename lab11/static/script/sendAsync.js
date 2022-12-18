

export default function sendData(data,url,isForm=true) {
    const XHR = new XMLHttpRequest();
    let form='';
    if(isForm){
        form = data;
        data=Object.fromEntries(new FormData(data));
    }
    let FD=new FormData();
    for (const [key, val] of Object.entries(data)) {
        FD.append(key, val);
    }

    XHR.addEventListener('load', (event) => {
        if(isForm) {
            new Response(XHR.response).json().then((value) => {
                let msg = form.querySelector('.message');
                msg.classList.add(value['add']);
                msg.textContent = value['msg'];
            });
        }
    });

    XHR.open('POST', `${url}`,false);
    XHR.send(FD);

    return XHR;
}
