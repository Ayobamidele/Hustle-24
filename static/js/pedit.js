// tabs
function openCity(evt, cityName) {
	var i, tabcontent, tablinks;
	tabcontent = document.getElementsByClassName("tabcontent");
	for (i = 0; i < tabcontent.length; i++) {
	  tabcontent[i].style.display = "none";
	}
	tablinks = document.getElementsByClassName("tablinks");
	for (i = 0; i < tablinks.length; i++) {
	  tablinks[i].className = tablinks[i].className.replace(" active", "");
	}
	document.getElementById(cityName).style.display = "block";
	evt.currentTarget.className += " active";
  }

  
  function openCity2(evt, cityName) {
	var i, tabcontent, tablinks;
	tabcontent = document.getElementsByClassName("tabcontent2");
	for (i = 0; i < tabcontent.length; i++) {
	  tabcontent[i].style.display = "none";
	}
	tablinks = document.getElementsByClassName("tablinks2");
	for (i = 0; i < tablinks.length; i++) {
	  tablinks[i].className = tablinks[i].className.replace(" active", "");
	}
	document.getElementById(cityName).style.display = "block";
	evt.currentTarget.className += " active";
  }
 

const chooseFile = document.getElementById("choose-file");
const imgPreview = document.getElementById("img-preview");

chooseFile.addEventListener("change", function () {
  getImgData();
});

function getImgData() {
  const files = chooseFile.files[0];
  if (files) {
    const fileReader = new FileReader();
    fileReader.readAsDataURL(files);
    fileReader.addEventListener("load", function () {
      imgPreview.style.display = "block";
      imgPreview.innerHTML = '<img name="choose-file" src="' + this.result + '" />';
    });    
  }
}





var priceInput = document.querySelector('input[type="price"]')
var dicsountPriceInput = document.querySelector('input[type="dicsount"]')

var currency = 'NGN' // https://www.currency-iso.org/dam/downloads/lists/list_one.xml

 // format inital value
onBlur({target:priceInput})
onBlur({target:dicsountPriceInput})

// bind event listeners
priceInput.addEventListener('focus', onFocus)
priceInput.addEventListener('blur', onBlur)

dicsountPriceInput.addEventListener('focus', onFocus)
dicsountPriceInput.addEventListener('blur', onBlur)

function localStringToNumber( s ){
  return Number(String(s).replace(/[^0-9.-]+/g,""))
}

function onFocus(e){
  var value = e.target.value;
  e.target.value = value ? localStringToNumber(value) : ''
}

function onBlur(e){
  var value = e.target.value

  var options = {
      maximumFractionDigits : 2,
      currency              : currency,
      style                 : "currency",
      currencyDisplay       : "symbol"
  }

  e.target.value = (value || value === 0) 
    ? localStringToNumber(value).toLocaleString(undefined, options)
    : ''
}
var categories = [];

var es = document.querySelectorAll('.input-categories');
for (var i = 0; i < es.length; i++) {
  es[i]._input = es[i].querySelector('input');
  es[i]._input._icategories = es[i];
  es[i].onkeydown = function(e){
    var e = event || e;
    if(e.keyCode == 13) {
      var c = e.target._icategories;
      if (categories.includes(c._input.value)) {
      	return c._input.value = '';
  	  }
      categories.push(c._input.value)
      // var li = document.createElement('li');

      // li.innerHTML = c._input.value;
      var li = '<li> %categoryValue% <span onclick="see()" class="icon icon-remove remove-category"></span><input type="hidden" name="categories" value="%categoryValue%"></li>';
      newHtml = li.replace(/%categoryValue%/g, c._input.value);
      document.querySelector('.input-categories ul').insertAdjacentHTML('beforeend', newHtml);
      c._input.value = '';
      e.preventDefault();
    }
  }
}


var removeCategoryBtns = document.getElementsByClassName('remove-category');
function see(e) {
    var e = event || e;
    var category = e.target.parentNode.innerText
    category = categories.indexOf(category)
    categories.splice(category)
    e.target.parentNode.remove()
    e.preventDefault();
}




// caching the elements
var titleInput = document.getElementById("title")
var h2 = document.getElementById("titleMessage")
// the main function: get the content from source and display it in destination
function display(source,destination)
{
  destination.textContent = source;
}

// events
titleInput.onkeyup=function(e)
{ 
	display(this.value,h2); 
  e.preventDefault();
};


var textareas = document.querySelectorAll('textarea');

document.getElementById('addProduct').addEventListener('keydown', function(e) {
  for (var i = 0; i < textareas.length; i++) {

    if (e.keyCode === 13 && e.target !== textareas[i]) {
      e.preventDefault();  
    }
  }
});