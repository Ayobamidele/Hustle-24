var newPassword = document.getElementById("id_password1");
var newPasswordRetype = document.getElementById("id_password2");
var copyPassword = document.getElementById("copy");
var suggestedPassword = document.getElementById("suggestedPassword");
var creditCardInput = document.getElementById("id_card_number");


function showPassword() {
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
    value = value.replace(/[^0-9]/g, "").substring(0, 24);
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


// viewOrderBtn = document.querySelectorAll(".viewOrders")
// orderlist = document.querySelectorAll(".orderlist")
// function getOrderTab() {

// }

// viewOrderBtn.onclick = console.log(viewOrderBtn)

// window.onload = function() {
//     var anchors = viewOrderBtn;
//     for(var i = 0; i < anchors.length; i++) {
//         var anchor = anchors[i];
//         anchor.onclick = function() {
//             console.log(anchor.attributes.dataid.value)
//             openCty(anchor.attributes.dataid.value)
//         }
//     }
// }


function openCty(order) {
    var element = document.getElementById(order);
    console.log(element)
    element.classList.toggle("show");
}



function openCtyVendor(order, order2, order3) {
    var element = document.getElementById(order);
    console.log(element)
    element.classList.toggle("show");

    var element2 = document.getElementById(order2);
    element2.classList.toggle("show");

    var element3 = document.getElementById(order3);
    element3.classList.toggle("show");
    
}

// $('form .autosubmit').on('change', function() {
//     this.form.submit();
//  });


// document.getElementById("id_profile_pic").onchange = function() {
//     document.getElementById("profilePicutureSetting").submit();
// };

// $('form .autosubmit').on('change', function() {
// // e.preventDefault();
// this.form.submit();
// $.ajax({
//     type: 'POST',
//     url: "{% url 'accounts:customer' request.user %}",
//     data: {
//                 form_type: "profilePicutureSetting",
//                 productqty: "wswstgvetuue",
//                 csrfmiddlewaretoken: "{{csrf_token}}",
//                 action: 'post'
//             },
//     success: function (json) {
//     alert("Successful Upload")
//     },
//     error: function (xhr, errmsg, err) {}
// });
// })