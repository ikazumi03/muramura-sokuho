(()=>{'use strict';
const openBtn=document.getElementById('navToggle'), nav=document.getElementById('navLinks');
if(openBtn&&nav){openBtn.addEventListener('click',()=>{const opened=nav.classList.toggle('open');openBtn.setAttribute('aria-expanded',String(opened));});}
const gate=document.getElementById('ageGate');
if(gate){const allowed=localStorage.getItem('muramura-sokuho-confirmed')==='yes';if(!allowed){gate.classList.add('open');document.body.style.overflow='hidden';}document.getElementById('ageYes')?.addEventListener('click',()=>{localStorage.setItem('muramura-sokuho-confirmed','yes');gate.classList.remove('open');document.body.style.overflow='';});document.getElementById('ageNo')?.addEventListener('click',()=>{document.querySelector('.agecard')?.classList.add('denied');});}
})();
