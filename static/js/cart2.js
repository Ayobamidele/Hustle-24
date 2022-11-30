// Test
// $(document).ready(function(){
//  alert('worked');
//  // ajax call here
// });

$(document).on('click', '.cart-add', function (e) {
    e.preventDefault();
    product = e.target.dataset['product']
    action = e.target.dataset['action']
    url = e.target.dataset['url']
    $.ajax({
      type: 'POST',
      url: url,
      data: {
        id: product,
        action: action,
        csrfmiddlewaretoken: csrftoken,
      },
      success: function (json) {
        console.log(json)
        document.getElementById("cart-total").innerHTML = json.qty
      },
      error: function (xhr, errmsg, err) {}
    });
})



url = "cart/status"
$.ajax({
  type: 'POST',
  url: url,
  data: {
    action: "get_status",
    csrfmiddlewaretoken: csrftoken,
  },
  success: function (json) {
    document.getElementById("cart-total").innerHTML = json.qty
  },
  error: function (xhr, errmsg, err) {}
});


function refresh() {
    $.ajax({
        url: 'cart/messages',
        type: 'GET',
        success: function(data) {
            let messagesHtml = "";
            for (var message of data.messages) {
              messagesHtml += `<div class="alert alert-info alert-dismissible fade show mx-auto w-80" role="alert">
              ${message}
              <button type="button" class="close fs-16 text-dark h-100" data-dismiss="alert" aria-label="Close">
                  <span aria-hidden="true" class="text-dark">&times;</span>
              </button>
          </div>`; // use your message html structure here
            }
            console.log(data)
            let messagesContainer = document.getElementById("messagesContainer");
            messagesContainer.innerHTML = messagesHtml;
            setTimeout(refresh, 2500);
        },
        error: function (xhr, errmsg, err) {
          console.log(err, errmsg, xhr)
        }
    });
}

$(function(){
    refresh();
});