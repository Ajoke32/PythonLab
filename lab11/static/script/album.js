import sendData from "./sendAsync.js";

let editDesc = document.getElementById('edit_desc');
let editName = document.getElementById('edit_name');
let decs = document.getElementById('desc');
let saveBth = document.getElementById('save');
let img = document.getElementById('img');
let audio = document.getElementById('audio');
let autdioDesc = document.getElementById('audio-desc');
let del = document.getElementById('delete');

let changedElements={};
window.addEventListener('click',()=>{
    console.log(changedElements);
})

img.oninput=(e)=>{
    if(img.files[0]){
        saveBth.style.display='block';
    }
}
audio.oninput=(e)=>{
    if(audio.files[0]){
        autdioDesc.style.display='flex';
        saveBth.style.display='block';
    }
}
editName.addEventListener('click', (e) => {
    let h2 = e.target.parentElement;
    let isInuput = h2.firstElementChild;
    if(isInuput.nodeName==='INPUT'){
        if(changedElements['albumname']===isInuput.value){
            delete changedElements['albumname'];
        }else{
            changedElements['albumname']=isInuput.value;
            saveBth.style.display='block';
        }
        h2.firstElementChild.remove();
        h2.textContent=isInuput.value;
        h2.append(e.target);
        return 0;
    }
    let input = document.createElement('input');
    let save = document.createElement('button')
    input.type = 'text';
    input.id = 'name';
    input.name = 'name';
    input.value = h2.textContent.trim();
    input.style.fontSize = '16px';
    changedElements['albumname']=h2.textContent.trim();
    h2.textContent = '';
    h2.append(input);
    input.focus();
    h2.append(e.target);
});
editDesc.addEventListener('click',(e)=>{
    let isArea = decs.firstElementChild;
    if(isArea){
        if(changedElements['description']===isArea.value){
            delete changedElements['description'];
        }else{
            changedElements['description']=isArea.value;
            saveBth.style.display='block';
        }
        decs.textContent=isArea.value;
        isArea.remove()
        return 0;
    }
    let textarea=document.createElement('textarea');
    textarea.value=decs.textContent.trim();
    changedElements['description']=decs.textContent.trim();
    decs.textContent='';
    textarea.name='newDesc';
    textarea.id='newDesc';
    decs.append(textarea);
    textarea.focus();
});

saveBth.addEventListener('click',(e)=>{

    if(img.files[0]){
        changedElements['img']=img.files[0];
    }
    let len =  Object.keys(changedElements).length;
    if(len>0) {
        sendData(changedElements, `update/${img.dataset['id']}`, false);
        changedElements={};
    }
    if(audio.files[0]){
        changedElements['song_name']=autdioDesc.firstElementChild.value;
        if(autdioDesc.firstElementChild.nextElementSibling.value) {
            changedElements['link'] = autdioDesc.firstElementChild.nextElementSibling.value;
        }else{
            changedElements['link']='';
        }
        changedElements['audio']=audio.files[0];
    }
    len =  Object.keys(changedElements).length;
    if(len>0) {
        sendData(changedElements, '/song/add', false);
        sendData({
            'song_name': changedElements['song_name']
            , 'album_id': img.dataset['id']
            , 'id': true
        }, 'entities/add', false);
    }
    saveBth.style.display='none';
});

del.addEventListener('click',()=>{
    let conf = confirm("Are you sure?");
    if(conf) {
        sendData({'del': 'true'}, `delete/${img.dataset['id']}`,false);
    }
});

