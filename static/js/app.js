var newPassword = document.getElementById("id_password1");
var newPasswordRetype = document.getElementById("id_password2");
var copyPassword = document.getElementById("copy");
var suggestedPassword = document.getElementById("suggestedPassword");
var creditCardInput = document.getElementById("id_card_number");

function showsearch() {
	var x = document.getElementById("myLinks");
	if (x.style.display === "block") {
	  x.style.display = "none";
	} else {
	  x.style.display = "block";
	}
  }

  



const imgs = document.querySelectorAll('.img-select a');
const imgBtns = [...imgs];
let imgId = 1;

imgBtns.forEach((imgItem) => {
  imgItem.addEventListener('click', (event) => {
	  event.preventDefault();
	  imgId = imgItem.dataset.id;
	  slideImage();
  });
});

function slideImage(){
  const displayWidth = document.querySelector('.img-showcase img:first-child').clientWidth;

  document.querySelector('.img-showcase').style.transform = `translateX(${- (imgId - 1) * displayWidth}px)`;
}



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


/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
function myFunction() {
document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(e) {
if (!e.target.matches('.dropbtn')) {
var myDropdown = document.getElementById("myDropdown");
  if (myDropdown.classList.contains('show')) {
	myDropdown.classList.remove('show');
  }
}
}
function showPassword() {
	if (newPassword.type === "password") {
		newPassword.type = "text";
	} else {
		newPassword.type = "password";
	}
}

function generatePassword() {
    var length = 24,
        charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
        retVal = "";
    for (var i = 0, n = charset.length; i < length; ++i) {
        retVal += charset.charAt(Math.floor(Math.random() * n));
    }
    return retVal;
}

suggestedPassword.textContent = generatePassword()

copyPassword.onclick = function() {
  copyPasswordToClipboard()
  showCopiedText()
};

function copyPasswordToClipboard() {
  var copyText = suggestedPassword.textContent
  /* Copy the text inside the text field */
  navigator.clipboard.writeText(copyText);  
}
function showCopiedText() {
  var popup = document.getElementById("myPopup");
  popup.classList.toggle("show");
}



creditCardInput.onkeydown = function(e) {
    var cursor = this.selectionStart;
    if (this.selectionEnd != cursor) return;
  
    if (e.which == 46) {
        if (this.value[cursor] == " ") this.selectionStart++;
    } else if (e.which == 8) {
        if (cursor && this.value[cursor - 1] == " ") this.selectionEnd--;
    }
  
}.oninput = function() {
    var value = this.value;
    var cursor = this.selectionStart;
  
    var matches = value.substring(0, cursor).match(/[^0-9]/g);
  
    if (matches) cursor -= matches.length;
    value = value.replace(/[^0-9]/g, "").substring(0, 16);
    var formatted = "";
    for (var i=0, n=value.length; i<n; i++) {
        if (i && i % 4 == 0) {
            if (formatted.length <= cursor) cursor++;
            formatted += " ";
        }
        formatted += value[i];
    }
    if (formatted == this.value) return;
  
    this.value = formatted;
    this.selectionEnd = cursor;
};

