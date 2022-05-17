// Adapted from CRS: http://www.surveysystem.com/sscalc.htm

conInt = 0;
conLev=1;
zVal=1.96;
zValC=3.8416;
ss=0;
pop=0;
perc=0;
pf = 0;

function to(obj) {

  if (obj.box.value == "") {
    conInt=0
  }
  else {
    conInt = eval(obj.box.value)
  }

  if (obj.popbox.value == "") { 
     pop=0
   }
  else {
     pop = eval(obj.popbox.value)
  }

  if (conInt == 0) {
      alert("You must enter a confidence interval between .1 and 50.")
   }
  else {  
     if (pop == 0) {
        ss = ((zVal *zVal) * 0.25) / ((conInt / 100) *(conInt / 100))
     }
     else {
       ss = ((zVal *zVal) * 0.25) / ((conInt / 100) *(conInt / 100));
       ss=ss/(1+(ss-1)/pop)
     }
        
     obj.ssbox.value=parseInt(ss+.5)

  }
}

function ConLevButF1(obj){
   zVal=1.96
}
function ConLevButF2(obj){
   zVal=2.58
}
function ConLevButFC1(obj){
   zValC=3.8416 ;
}
function ConLevButFC2(obj){
   zValC=6.6564 ;
}
function cler(obj, string) {
  obj.box.value = string;
  obj.popbox.value = string;
  obj.ssbox.value = string;
}

function ct(obj) {
    if (obj.pbox.value == "") { 
     pnt = 0
     }
     else {
     pnt = eval(obj.pbox.value)
     }
  
     cst = (pnt * .028);
     obj.cbox.value=parseInt(cst)
  }