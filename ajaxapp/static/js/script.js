$("#friend-form").submit(function (e) {
    // preventing from page reload and default actions
    e.preventDefault();
    // serialize the data for sending the form data.
    // The serialized values can be used in the URL query string when making an AJAX request
    var serializedData = $(this).serialize();
    // make POST ajax call
    $.ajax({
        type: 'POST',
        url: "{% url 'post_friend' %}",
        data: serializedData,
        success: function (response) {
            // on successfull creating object
            // 1. clear the form.
            $("#friend-form").trigger('reset');
            // 2. focus to nickname input 
            $("#id_nick_name").focus();

            // display the newly friend to table.
            var instance = JSON.parse(response["instance"]);
            var fields = instance[0]["fields"];
            $("#my_friends tbody").prepend(
                `<tr>
                <td>${fields["nick_name"]||""}</td>
                <td>${fields["first_name"]||""}</td>
                <td>${fields["last_name"]||""}</td>
                <td>${fields["likes"]||""}</td>
                <td>${fields["dob"]||""}</td>
                <td>${fields["lives_in"]||""}</td>
                </tr>`
            )
        },
        error: function (response) {
            // alert the error if any error occured
            alert(response["responseJSON"]["error"]);
        }
    })   
})


 /*
    On focus out on input nickname,
    call AJAX get request to check if the nickName
    already exists or not.
    */
$("#id_nick_name").focusout(function (e) {
    e.preventDefault();
    // get the nickname
    var nick_name = $(this).val();
    // GET AJAX request
    $.ajax({
        type: 'GET',
        url: "{% url 'validate_nickname' %}",
        data: {"nick_name": nick_name},
        success: function (response) {
            // if not valid user, alert the user
            if(!response["valid"]){
                alert("You cannot create a friend with same nick name");
                var nickName = $("#id_nick_name");
                nickName.val("")
                nickName.focus()
            }
        },
        error: function (response) {
            console.log(response)
        }
    })
})