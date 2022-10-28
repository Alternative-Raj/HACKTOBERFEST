let i = 1;
let slider = document.querySelectorAll('slides'); 
next=document.getElementById("next")
prev=document.getElementById("prev")

next.addEventListener('click',function () {
    i++;
    if (i>4) {
        i=4;
        image.src=`./images/image${i}.jpg`;

    } else {
        image.src=`./images/image${i}.jpg`;
    }
    
});

prev.addEventListener('click',function () {
    i--;
    
    if (i<=0) {
        i=1;
        image.src=`./images/image${i}.jpg`;   

    } else {
        image.src=`./images/image${i}.jpg`;   

    }
    
});

