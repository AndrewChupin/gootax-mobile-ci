/**
 * Created by gootax on 10.07.17.
 */
/**
 * Created by gootax on 29.06.17.
 */


(function ($) {
    let app = {
        appForm: '#saveApplication',
        init: function () {
            this.registerFormSubmitEvent();
        },
        registerFormSubmitEvent() {
            $(this.appForm).on('submit', function () {
                $.ajax({
                    type: 'POST', url: '/driver_app_save', data: $('#saveApplication').serialize(),
                    success: function (response) {
                        parseAction(response)
                    }
                });
                return false
            });
        }
    };
    app.init();
})(jQuery);

function parseAction(action) {
    let json_action = $.parseJSON(action);
    console.log(json_action);
    switch (json_action.action) {
        case "redirect":

            let url = json_action.data.url;
            if (url) {
               window.location = url
            }
            break;
        case "error":
            let message = json_action.data.message;
            if (message) {
                 console.log(json_action);
                alert(message)
            }
            break;
        default:
            break;
    }
}


$("select[name=app_type]").on('change', function () {
    let type = $(this).val();
    onUpdateBuildType(type);
});


function onUpdateBuildType(type) {
    console.log("init platform " + type);
    let use_sms_auth = $('.js-use-sms-auth');

    switch (type) {
        case "1": // Gootax
            use_sms_auth.hide();
            $('.js-use-sms-auth-check').prop("checked", false);
            break;
        case "2": // Индивидуальная
            use_sms_auth.show();
            break;
        default:
            console.log("Unknown type");
            break;
    }
}