let button=document.getElementById("result-button");
let button1=document.querySelector('.btn__continue');

button.addEventListener('click' , ()=>{
    document.querySelector('#main-id').classList.add('main');
    document.querySelector('.container-result-off').classList.add('container-result-on');
    document.querySelector('.container-result-off').classList.remove('container-result-off');
})

button1.addEventListener('click' , ()=>{
    document.querySelector('#main-id').classList.remove('main');
    document.querySelector('.container-result-on').classList.add('container-result-off');
    document.querySelector('.container-result-off').classList.remove('container-result-on');
})

//banner span typewriting animation
var typed=new Typed(".auto-type" , {
    strings:["Everything your college does , we digitilize it.",
     "Transforming Education " , "Evelate Your Eduction" ,"Discover Academic Excellence"],
    typeSpeed:80,
    backSpeed:20,
    loop:true
})

const toastTrigger = document.getElementById('liveToastBtn')
const toastLiveExample = document.getElementById('liveToast')

if (toastTrigger) {
  const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)
  toastTrigger.addEventListener('click', () => {
    toastBootstrap.show()
  })
}

// testimonials

$(".card").hover(
  function () {
    $(this).siblings(".card").addClass("card-blur");
  },
  $(".card").hover(function () {
    $(this).siblings(".card").removeClass("card-blur");
  })
);

// routing

// const r=document.querySelector(".hover-underline-animation");
// r.addEventListener('click' , ()=>{
//   console.log(window.location.href);
//   if(window.location.href==="http://127.0.0.1:5500/landing-page.html"){
//     window.location.href="home.html";
//     alert("LOGEED IN SUCCESSFULLY");
//     }
//   else{
//     window.location.href="landing-page.html";
//     alert("LOGEED OUT SUCCESSFULLY");

//   }

// })


//news section read more error for before login

const read=document.querySelectorAll('.read-more').forEach(item =>{
  item.addEventListener('click' , ()=>{
    alert("sign up first");
  })
})

//loader screen

function spinOff(){
  document.querySelector('#load').classList.remove("loading-screen");
  document.querySelector('#load').classList.add("loading-screen-off");
  document.querySelector('.bg-light').classList.remove("navbarOff");
}
function spinOn(){
  document.querySelector('#load').classList.remove("loading-screen-off");
  document.querySelector('#load').classList.add("loading-screen");
  document.querySelector('.bg-light').classList.add("navbarOff");

}

// check for internet and and loader after refresh

let check=true;
document.addEventListener('DOMContentLoaded', ()=>{
  checkInternet();
  if(check){
  document.getElementById("loader-text").innerText="Loading Content...";
  spinOn();
  setTimeout(spinOff,1500);
  }
})

function checkInternet(){
  if(navigator.onLine){
    spinOff();
    check=true;
  }
  else{
    spinOn();
    check=false;
  }

  
}
