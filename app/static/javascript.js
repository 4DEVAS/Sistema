(function(win,doc){
    'use strict';

    //Verificar a deleção do dado
    if(doc.querySelector('.btnDel')){
        let btnDel = doc.querySelectorAll('.btnDel');
        for(let i=0; i < btnDel.length; i++){
            btnDel[i].addEventListener('click', function(event){
                if(confirm('Você está preste a excluir este dado. Ao confirmar, será excluido definitivamente. Confirmar?')){
                    return true;
                }else{
                    event.preventDefault();
                }
            });
        }
    }

    //Ajax do form
    if(doc.querySelector('#form')){
        let form=doc.querySelector('#form');
        function sendForm(event)
        {
            event.preventDefault();
            let data = new FormData(form);
            let ajax = new XMLHttpRequest();
            let token = doc.querySelectorAll('input')[0].value;
            ajax.open('POST', form.action);
            ajax.setRequestHeader('X-CSRF-TOKEN',token);
            ajax.onreadystatechange = function()
            {
                if(ajax.status === 200 && ajax.readyState === 4){
                    let result = doc.querySelector('#result');
                    result.innerHTML = 'Operação realizada com sucesso!';
                    result.classList.add('alert');
                    result.classList.add('alertsuccess');

                }
            }
            ajax.send(data);
            form.reset();
        }
        form.addEventListener('submit',sendForm,false);
    }
})(window,document);