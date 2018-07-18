
// variables



  const product = {

    lifeEvo: 0.70,

    xepressLife: 0.50,

    pension: 0.25,
};

eventListeners()
// event listeners
function eventListeners() {
   document.querySelector('#form').addEventListener('submit',premium)
   //document.querySelector('productlist').addEventListener('click',productList)

}








// functions
function premium (e){
    e.preventDefault();
    const userinput = document.getElementById('userinput').value;
    let product = 0.70;
    let commission;
    commission = product * userinput * 12;
    document.getElementById('userinput').value = Math.round(commission);
    console.log(commission);



 }
