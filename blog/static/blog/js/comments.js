document.addEventListener("DOMContentLoaded", function() {
    const commentText = document.getElementById("id_body");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteConfirm = document.getElementById("deleteConfirm");

   //For editing of comments
    for (let button of document.querySelectorAll(".btn-edit[comment_id]")){
      button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        let commentContent = document.getElementById(`comment${commentId}`).innerText;
        commentText.value = commentContent;
        submitButton.innerText = "Update";
        commentForm.setAttribute("action", `edit_comment/${commentId}`);
      });
    };

    //For deletion of commnts
    document.querySelectorAll(".btn-delete[comment_id]").forEach(button => {
      button.addEventListener("click", (e) => {
        e.preventDefault();
        const commentId = e.target.getAttribute("comment_id");
        deleteConfirm.href = `delete_comment/${commentId}`;
        deleteModal.show();
      });
    });



    //For deletion of Posts
    document.querySelectorAll(".btn-delete[post_id]").forEach(button => {
      button.addEventListener("click", (e) => {
        e.preventDefault();
        const postId = e.target.getAttribute("post_id");
        deleteConfirm.href = `/post/${postId}/delete/`;
        deleteModal.show();
      });
    });


    document.getElementById('deleteModal').addEventListener('hidden.bs.modal', function () {
      document.querySelector('.modal-backdrop').remove();
    });
  });