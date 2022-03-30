package com.softwarechaser.springboot.tutorial.service;


import java.util.List;
import java.util.Objects;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.softwarechaser.springboot.tutorial.entity.Department;
import com.softwarechaser.springboot.tutorial.repository.DepartmentRepository;

@Service
public class DepartmentServiceImpl implements DepartmentService {
	@Autowired
	private DepartmentRepository departmentRepository;
	@Override
	public Department saveDepartment(Department department)
	{
		return departmentRepository.save(department);
	}
	@Override
	public List<Department> fetchDepartmentList() {
		return departmentRepository.findAll();
	}
	@Override
	public Department fetchDepartmentById(Long QId) {
		// TODO Auto-generated method stub
		return departmentRepository.findById(QId).get();
	}
	@Override
	public void deleteDepartmentById(Long QId) {
		// TODO Auto-generated method stub
		departmentRepository.deleteById(QId);
		
	}
	
	@Override
	public Department updateDepartment(Long QId, Department department) {
		// TODO Auto-generated method stub
		Department depDB = departmentRepository.findById(QId).get();
		if(Objects.nonNull(department.getQuestion()) &&!"".equalsIgnoreCase(department.getQuestion()))
		{
			depDB.setQuestion(department.getQuestion());
		}
		if(Objects.nonNull(department.getCategory()) && !"".equalsIgnoreCase(department.getCategory()))
		{
			depDB.setQuestion(department.getCategory());
		}
		
		return departmentRepository.save(department);
	}
	
	

}
