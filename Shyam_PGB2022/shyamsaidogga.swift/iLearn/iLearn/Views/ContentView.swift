//
//  ContentView.swift
//  iLearn
//
//  Created by Shyam sai Dogga on 24/03/22.
//

import SwiftUI

struct ContentView: View {
    @StateObject var ilearnManager = iLearnManager()
    @StateObject var jsManager = JsManager()
    
    
    var body: some View {
        NavigationView {
           
            VStack( spacing: 40) {
                    HStack(spacing: 20){
                    VStack(spacing: 20) {
                    Text("iSpace")
                        .lilacTitle()
                    Text("THE LEARNING APP")
                        .foregroundColor(.black)
                    }
                
                        
                }
                    
                VStack(alignment: .leading,spacing:20){
                Text("Ready for the Challenge?")
                        .foregroundColor(Color("AccentColor"))
                    Text("")
                }
                
                NavigationLink {
                    iLearnView()
                        .environmentObject(ilearnManager)
                        .transition(AnyTransition.opacity.animation(.easeIn))
                } label: {
                    PrimaryButton(text: "Java")
                }
                
                NavigationLink {
                    JsView()
                        .environmentObject(jsManager)
                } label: {
                    PrimaryButton(text: "Java-Script")
                }
                    
            }
    
            }
            .frame(maxWidth: .infinity, maxHeight: .infinity)
            .edgesIgnoringSafeArea(.all)
            .background(.white)
            
        
    }
        
    
    
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        Group {
            ContentView()
            ContentView()
        }
    }
}
