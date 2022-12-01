// Test
// $(document).ready(function(){
//  alert('worked');
//  // ajax call here
// });

$(document).on('click', '.cart-add', function (e) {
    e.preventDefault();
    product = e.target.dataset['product']
    action = e.target.dataset['action']
    url = 'cart/add'
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

// $(document).on('click', '.cart-remove', function (e) {
//     e.preventDefault();
//     product = e.target.dataset['product']
//     action = e.target.dataset['action']
//     url = "cart/remove"
//     console.log("Success here")
//     $.ajax({
//       type: 'POST',
//       url: url,
//       data: {
//         id: product,
//         action: action,
//         csrfmiddlewaretoken: csrftoken,
//       },
//       success: function (json) {
//         console.log(json)
//         document.getElementById("cart-total").innerHTML = json.qty
//       },
//       error: function (xhr, errmsg, err) {}
//     });
// })

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


