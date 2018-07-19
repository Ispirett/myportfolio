
// LifeProducts object



  const LifeProducts = {
    // life
    lifeEvo: 0.70,

    xpressLife: 0.50,

    flexiTerm: 0.25,

    ecnoLife: 0.50,

  };


 const PesionProducts = {

     ipi: 0.05,
     pension: 0.30,



 };


 const PresidiaProducts = {


     accident: 0.20,



 };

















const products2 = document.querySelectorAll('#pContainer option:nth-child(9)');
     console.log(products2);




//
const premiumCal = () => {

    const products = document.getElementById('productlist');

     if (products.value === 'le') {
         console.log( "1");
         premium(LifeProducts.lifeEvo);

     }

     if (products.value === 'xl') {
         console.log("2");
         premium(LifeProducts.xpressLife);
     }


      if (products.value === 'ft') {
          console.log('3');
          premium(LifeProducts.flexiTerm);
      }

       if (products.value === 'el') {
         console.log('4');
         premium(LifeProducts.ecnoLife)
     }

// pension products
const pensionProducts = document.getElementById('p0');

       if (pensionProducts.value === 'ipi') {
          console.log('1');
          premium(PesionProducts.ipi);
      }

       if (pensionProducts.value === 'pen') {
         console.log('2');
          premium(PesionProducts.pension)
     }

// personal Accident
const presidiaProducts = document.getElementById('p2');


       if (presidiaProducts.value === 'pa') {
          console.log('1');
          premium(PresidiaProducts.accident);
      }



};















const commissionCal = () => {
// life lifeProducts
    const lifeProducts = document.getElementById('productlist');

     if (lifeProducts.value === 'le') {
         console.log( "1");
         commission(LifeProducts.lifeEvo);

     }

     if (lifeProducts.value === 'xl') {
         console.log("2");
        commission(LifeProducts.xpressLife);
     }


      if (lifeProducts.value === 'ft') {
          console.log('3');
          commission(LifeProducts.flexiTerm);
      }

       if (lifeProducts.value === 'el') {
         console.log('4');
         commission(LifeProducts.ecnoLife)
     }


// pension products
const pensionProducts = document.getElementById('p0');

       if (pensionProducts.value === 'ipi') {
          console.log('1');
          premium(PesionProducts.ipi);
      }

       if (pensionProducts.value === 'pen') {
         console.log('2');
          commission(PesionProducts.pension)
     }

// personal Accident
const presidiaProducts = document.getElementById('p2');


       if (presidiaProducts.value === 'pa') {
          console.log('1');
          commission(PresidiaProducts.accident);
      }




};





















// functions
function premium (product){


    const userinput = document.getElementById('userinput').value;
    let commission;
    commission = product * userinput * 12;
    document.getElementById('userinput').value = Math.round(commission);
    console.log(commission);



 }

const commission = (product) => {


    let com = document.getElementById('userinput').value;

    let answer = com / product / 12;
    document.getElementById('userinput').value = Math.round(answer);
    console.log(answer);


 };

