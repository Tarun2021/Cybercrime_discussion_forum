function handletheReplybutton(responseid) {
    const replyformcontainer = document.getElementById('reply_form_container-${responseid}');
    if (replyformcontainer) {
        replyformcontainer.className = 'reply_form_container enabled';
    }
}

function handleCancelReply(responseId) {
    const replyFormContainer = document.getElementById(`reply-form-container-${responseId}`);
    if (replyFormContainer) {
        replyFormContainer.className = 'reply-form-container'
    }
}