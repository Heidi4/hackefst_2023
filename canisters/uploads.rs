use ic_cdk_macros::{query, update};

#[derive(Serialize, Deserialize)]
struct UploadData {
    filename: String,
    content_type: String,
    data: Vec<u8>,
}

#[update]
fn upload_file(upload_data: UploadData) -> Result<String, String> {
    // Implement logic to store the uploaded file
    // ...

    Ok("File uploaded successfully".to_string())
}