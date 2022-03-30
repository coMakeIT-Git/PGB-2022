package com.softwarechaser.springboot.tutorial.service;

import java.util.List;

import org.springframework.stereotype.Service;

import com.softwarechaser.springboot.tutorial.entity.Department;
@Service
public interface DepartmentService {

	public Department saveDepartment(Department department);

	public List<Department> fetchDepartmentList();

	public Department fetchDepartmentById(Long QId);

	public void deleteDepartmentById(Long QId);

	public Department updateDepartment(Long QId,Department department);

}
