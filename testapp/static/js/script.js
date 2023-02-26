$(document).ready( function() {
    $("#index_form").on('load', read())
    $("#create").on('click', function(e) {
        e.preventDefault()
        let firstname  = $("#firstname").val()
        let lastname  = $("#lastname").val()
        let csrf = $('input[name=csrfmiddlewaretoken]').val()
        $.ajax({
            url: 'create/',
            type: "post",
            data: {
                firstname: firstname,
                lastname: lastname,
                csrfmiddlewaretoken:csrf
            },
            success: function() {
                read()
                alert("success")
            }
        })
    })
})
function edit(id) {
    window.location = 'edit/'+id
}

function deleteuser(id) {
    
    alert(id)
    $.ajax({
        url: 'delete/'+id,
        type: 'post',
        data: {csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()},
        success: function(data) {
            if(data == 'success') {
                read()
            }
        }
    })
}

$("#update").on('click', function(e){
    e.preventDefault()
    let id  = $("#member_id").val()
    let firstname  = $("#firstname_").val()
    let lastname  = $("#lastname_").val()
    let csrf = $('input[name=csrfmiddlewaretoken]').val()
    $.ajax({
        url: 'update/'+id,
        type: "post",
        data: {
            firstname: firstname,
            lastname: lastname,
            csrfmiddlewaretoken:csrf
        },
        success: function(data) {
            // window.location = '/'
            alert(data)
            if(data == 'success') {
                window.location= '/'
            }
        }
    })
})
function read() {
    $.ajax({
        url: 'read/',
        type: 'post',
        data: {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(data) {
            $("#result").html(data)
        }
    })
}