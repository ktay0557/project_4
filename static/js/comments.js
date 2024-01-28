const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/** 
 * Gives functionality to the edit button in comments section.
 * 
 * Allows user to edit their previous comments by:
 * - Retrieving the comment's ID when clicked.
 * - Fetching the content of the comment.
 * - Populating the `commentText` input area with the comment for editting.
 * - Updates the submit button when editing to 'update'.
 * - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
 */

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("data-comment_id");
        let commentContent = document.getElementById(`comment${commentId}`).innerText;
        commentText.value = commentContent;
        submitButton.innerText = "Update";
        commentForm.setAttribute("action", `edit_comment/${commentId}`);
    });
}

/** 
 * Gives functionality to the delete button in comments section.
 * 
 * Allows user to delete their previous comments by:
 * - Retrieving the comment's ID when clicked.
 * - Updates the `deleteConfirm` link href to allow for specific comment.
 * - Displays confirmation modal to ensure the user confirms before deleting.
 */

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("data-comment_id");
        deleteConfirm.href = `delete_comment/${commentId}`;
        deleteModal.show();
    });
}