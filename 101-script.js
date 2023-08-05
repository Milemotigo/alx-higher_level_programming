$(document).ready(function() {
    $("#add_item").click(function() {
        let my_list = $("<li>newItem</li>");
        $(".my_list").append(my_list);
    });
    $("remove_item").click(function() {
        let list = $(".my_list list:last-child");
        list.remove();
    })
    $("#clear_list").click(function() {
        my_list = $(".my_list");
        my_list.empty();
    })
})