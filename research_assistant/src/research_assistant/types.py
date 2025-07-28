from typing import List, Optional
from pydantic import BaseModel, Field


class TaskEstimate(BaseModel):
    task_name: str = Field(..., description="Name of the content task")
    format: str = Field(..., description="Content format (e.g., blog, video, email)")
    estimated_time_hours: float = Field(..., description="Estimated time to complete the task in hours")
    required_resources: List[str] = Field(..., description="List of resources needed (roles/tools)")
    target_publish_date: Optional[str] = Field(None, description="Planned publish date (YYYY-MM-DD)")
    dependencies: Optional[List[str]] = Field(default_factory=list, description="IDs or names of dependent tasks")


class TaskAssignment(BaseModel):
    task_name: str = Field(..., description="Name of the content task")
    assigned_to: str = Field(..., description="Name of the team member assigned")
    role: str = Field(..., description="Role of the assigned team member (e.g., writer, editor)")
    start_date: Optional[str] = Field(None, description="Planned start date (YYYY-MM-DD)")
    end_date: Optional[str] = Field(None, description="Planned end date (YYYY-MM-DD)")
    justification: Optional[str] = Field(None, description="Reason this team member was assigned")



class ProjectPlan(BaseModel):
    assignments: List[TaskAssignment] = Field(..., description="Task-to-person assignments with scheduling")
    
