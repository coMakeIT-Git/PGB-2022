package com.softwarechaser.springboot.tutorial.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.softwarechaser.springboot.tutorial.entity.Department;
import com.softwarechaser.springboot.tutorial.service.DepartmentService;

@RestController
public class DepartmentController {
	@Autowired
	private DepartmentService departmentService;
	@PostMapping("/questions")
	public Department saveDepartment(@RequestBody Department department)
	{
		return departmentService.saveDepartment(department);
	}
	@GetMapping("/questions")
	public List<Department> fetchDepartmentList()
	{
		return departmentService.fetchDepartmentList();
	}
	@GetMapping("/questions/{id}")
	public Department fetchDepartmentById(@PathVariable("id") Long QId)
	{
		return departmentService.fetchDepartmentById(QId);
	}
	@DeleteMapping("/questions/{id}")
	public String deleteDepartmentById(@PathVariable("id") Long QId)
	{
		departmentService.deleteDepartmentById(QId);
		return "Department deleted successfully";
	}
	@PutMapping("/questions/{id}")
	public Department updateDepartment(@PathVariable("id") Long QId,@RequestBody Department department)
	{
		return departmentService.updateDepartment(QId,department);
	}

}
