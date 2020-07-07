

resource "aws_cloudwatch_log_group" "shared_autopatch" {
  name = "shared_autopatch"
  retention_in_days = 120
  tags = {
    Environment = "shared_prod"
    Application = "shared_autopatch"
  }
}

resource "aws_cloudwatch_log_stream" "autopatch" {
  name           = "autopatch"
  log_group_name = "${aws_cloudwatch_log_group.shared_autopatch.name}"
}

resource "aws_cloudwatch_log_metric_filter" "autopatch_success" {
  name           = "auto_patch_success"
  pattern        = "BACKUP_COMPLETED"
  log_group_name = "${aws_cloudwatch_log_group.shared_autopatch.name}"

  metric_transformation {
    name      = "BACKUP_COMPLETED"
    namespace = "shared_autopatch"
    value     = "1"
  }
}