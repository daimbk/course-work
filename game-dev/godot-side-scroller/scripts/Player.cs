using Godot;
using System;

public partial class Player : CharacterBody2D
{
	public const float Speed = 130.0f;
	public const float JumpVelocity = -300.0f;
	public int health = 100;
	public int lives = 3;

	// Get the gravity from the project settings to be synced with RigidBody nodes.
	public float gravity = ProjectSettings.GetSetting("physics/2d/default_gravity").AsSingle();
	private AnimatedSprite2D animSprite;
	private GameManager gameManager;
	public Label uiLabel;

	public override void _Ready()
	{
		gameManager = (GameManager)GetNode("/root/GameManager");
		animSprite = GetNode<AnimatedSprite2D>("/root/Game/Player/AnimatedSprite2D");
		initStats();
		uiLabel = GetNode<Label>("/root/Game/Player/ui");
	}

	public override void _PhysicsProcess(double delta)
	{
		Vector2 velocity = Velocity;

		// Add the gravity.
		if (!IsOnFloor()){
			velocity.Y += gravity * (float)delta;
			animSprite.Play("jump");
		}
		// Handle Jump.
		if (Input.IsActionJustPressed("jump") && IsOnFloor()){
			velocity.Y = JumpVelocity;
		}

		float direction = Input.GetAxis("move_left", "move_right");
		if (direction < 0)
		{
			animSprite.FlipH = true;
		}
		else if (direction > 0)
		{
			animSprite.FlipH = false;
			
		}
		if (IsOnFloor()){
			if(direction == 0){
				animSprite.Play("idle");
			}
			else{
				animSprite.Play("run");
			}
		}

		velocity.X = direction * Speed;

		Velocity = velocity;
		MoveAndSlide();
		
		DisplayUI();
	}
	
	public void initStats()
	{
		health = 100;
		lives = 3;
	}
	
	public void DisplayUI()
	{
		uiLabel.Text = "Health: " + health + "\nLives: " + lives + "\nScore: " + gameManager.Score;
	}
	
	public void ReduceHealth(int amount)
	{
		health -= amount;
		if (health <= 0)
		{			
			lives -= 1;
			if (lives == 0)
			{
				GD.Print("Game Over!");
				//gameManager.GotoScene("res://scenes/GameOver.tscn");
				CallDeferred("SwitchToGameOverScene");
			}
			
			health = 100;
		}
		GD.Print("Health: " + health + " Lives: " + lives);
	}
	
	private void SwitchToGameOverScene()
	{
		GetTree().ChangeSceneToFile("res://scenes/GameOver.tscn");
	}
}
